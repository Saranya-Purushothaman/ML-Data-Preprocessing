🧩 MixAR Preprocessing Solution
🔍 Overview
The MixAR Preprocessing Tool is a Python utility for preparing 3D mesh models (.obj files) for AR/VR or ML workflows.
It performs loading, normalization, duplicate removal, and structured data export, ensuring models are clean and consistent.

⚙️ Usage
Command:
python mixar_preprocess.py --input path/to/model.obj --output output/processed_model.npz
Example:
python mixar_preprocess.py --input diamond.obj --output output/processed_diamond.npz

🧠 Processing Steps
Step	Description
1. Load OBJ File	Reads the 3D geometry using the trimesh library.
2. Normalize Vertices	Centers the model at the origin and scales it to a unit cube.
3. Remove Duplicates	Removes redundant vertices and updates face indices.
4. Save Processed Data	Exports the cleaned vertices and faces as a .npz file.
📦 Output

Processed data is saved as a compressed NumPy file:
output/processed_model.npz

Contents-
vertices: normalized 3D vertex coordinates
faces: polygonal face indices (if available)

Load Example:
import numpy as np
data = np.load('output/processed_diamond.npz')
verts = data['vertices']
faces = data['faces']

🧰 Requirements
Install dependencies:
pip install numpy trimesh

(Optional: create a virtual environment)
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # macOS/Linux

🧾 Example Console Output
📦 Loading OBJ file: diamond.obj
✅ Loaded 2456 vertices and 3200 faces.
🎯 Vertices normalized (centered at origin, scaled to unit size).
🧹 Removed 12 duplicate vertices.
💾 Saved processed data to: output/processed_diamond.npz
🎉 Preprocessing completed successfully.

🧘 Notes
Works with .obj files containing vertex (v) and face (f) data.
Ignores lines like s (smoothing groups) automatically.
Output is ready for AR frameworks or 3D ML pipelines
