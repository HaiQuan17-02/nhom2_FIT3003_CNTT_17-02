class Edge:
    def __init__(self, u, v, weight):
        self.u = u  # Đỉnh đầu tiên
        self.v = v  # Đỉnh thứ hai
        self.weight = weight  # Trọng số (chi phí)

    def __lt__(self, other):
        return self.weight < other.weight

class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices  # Danh sách các đỉnh
        self.parent = {v: v for v in vertices}  # Tập hợp cha ban đầu
        self.rank = {v: 0 for v in vertices}  # Độ sâu của cây

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Tìm cha gốc
        return self.parent[vertex]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

    def kruskal(self, edges):
        edges.sort()  # Sắp xếp các cạnh theo trọng số tăng dần
        mst = []  # Lưu danh sách các cạnh trong cây khung tối thiểu
        total_cost = 0  # Tổng chi phí của cây khung tối thiểu

        for edge in edges:
            root1 = self.find(edge.u)
            root2 = self.find(edge.v)

            # Chỉ thêm cạnh vào MST nếu không tạo thành chu trình
            if root1 != root2:
                mst.append(edge)
                total_cost += edge.weight
                self.union(root1, root2)

        return mst, total_cost

# Dữ liệu đầu vào: danh sách các cạnh với chi phí
edges_data = [
    ('A1', 'A2', 0.05),
    ('A1', 'A3', -0.02),
    ('A2', 'A4', 0.03),
    ('A2', 'A5', 0.04),
    ('A3', 'A6', 0.01),
    ('A3', 'A7', -0.01),
    ('A4', 'A8', 0.06),
    ('A4', 'A9', 0.02),
    ('A5', 'A10', 0.03),
    ('A5', 'A11', -0.04),
    ('A6', 'A12', 0.05),
    ('A6', 'A13', 0.02),
    ('A7', 'A14', 0.07),
    ('A8', 'A15', -0.03),
    ('A9', 'A16', 0.01),
    ('A10', 'A17', 0.04),
    ('A11', 'A18', 0.02),
    ('A12', 'A19', -0.01),
    ('A13', 'A20', 0.03),
    ('A14', 'A21', 0.05),
    ('A15', 'A22', 0.06),
    ('A16', 'A23', -0.02),
    ('A17', 'A24', 0.04),
    ('A18', 'A25', 0.03),
    ('A19', 'A26', 0.02),
    ('A20', 'A27', -0.03),
    ('A21', 'A28', 0.05),
    ('A22', 'A29', 0.04),
    ('A23', 'A30', -0.01),
    ('A24', 'A31', 0.03),
    ('A25', 'A32', 0.06),
    ('A26', 'A33', 0.01),
    ('A27', 'A34', -0.02),
    ('A28', 'A35', 0.04),
    ('A29', 'A36', 0.05),
    ('A30', 'A37', 0.03),
    ('A31', 'A38', -0.01),
    ('A32', 'A39', 0.04),
    ('A33', 'A40', 0.06),
    ('A34', 'A41', -0.03),
    ('A35', 'A42', 0.02),
    ('A36', 'A43', 0.05),
    ('A37', 'A44', 0.03),
    ('A38', 'A45', -0.02),
    ('A39', 'A46', 0.04),
    ('A40', 'A47', 0.05),
    ('A41', 'A48', -0.01),
    ('A42', 'A49', 0.03),
    ('A43', 'A50', 0.06),
    ('A44', 'A1', 0.02),
    ('A45', 'A2', 0.05),
    ('A46', 'A3', -0.01),
    ('A47', 'A4', 0.03),
    ('A48', 'A5', 0.04),
    ('A49', 'A6', -0.03),
    ('A50', 'A7', 0.01),

]

# Chuyển đổi dữ liệu thành danh sách các cạnh
edges = [Edge(u, v, weight) for u, v, weight in edges_data]

# Lấy danh sách các đỉnh từ dữ liệu đầu vào
vertices = set()
for u, v, _ in edges_data:
    vertices.add(u)
    vertices.add(v)

# Áp dụng thuật toán Kruskal
kruskal = Kruskal(vertices)
mst, total_cost = kruskal.kruskal(edges)

# In kết quả
print("Các kết nối trong mạng tối ưu:")
for edge in mst:
    print(f"{edge.u} - {edge.v} (Chi phí: {edge.weight})")

print(f"Tổng chi phí lắp đặt: {total_cost}")
