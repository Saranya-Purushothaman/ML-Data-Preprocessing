import os
import numpy as np
import trimesh


def load_obj(path):
    """Load an OBJ file and extract vertices and faces."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    print(f"📦 Loading OBJ file: {path}")
    mesh = trimesh.load(path, process=False)

    # Extract vertices and faces
    if not hasattr(mesh, 'vertices'):
        raise ValueError("Loaded object has no vertices")

    verts = np.asarray(mesh.vertices, dtype=np.float64)
    faces = np.asarray(mesh.faces, dtype=np.int32) if hasattr(mesh, 'faces') else None
    print(f"✅ Loaded {len(verts)} vertices and {len(faces) if faces is not None else 0} faces.")
    return verts, faces


def normalize_vertices(verts):
    """Normalize vertices around origin and scale to unit cube."""
    if verts is None or len(verts) == 0:
        raise ValueError("No vertices to normalize")

    min_vals = np.min(verts, axis=0)
    max_vals = np.max(verts, axis=0)
    center = (min_vals + max_vals) / 2.0
    scale = np.max(max_vals - min_vals)

    normalized = (verts - center) / scale
    print("🎯 Vertices normalized (centered at origin, scaled to unit size).")
    return normalized


def remove_duplicate_vertices(verts, faces):
    """Remove duplicate vertices and update face indices."""
    unique_verts, inverse_indices = np.unique(np.round(verts, 6), axis=0, return_inverse=True)
    updated_faces = inverse_indices[faces] if faces is not None else None
    removed = len(verts) - len(unique_verts)
    print(f"🧹 Removed {removed} duplicate vertices.")
    return unique_verts, updated_faces


def save_processed_data(verts, faces, out_path):
    """Save preprocessed vertices/faces into a compressed NumPy file."""
    np.savez(out_path, vertices=verts, faces=faces)
    print(f"💾 Saved processed data to: {out_path}")


def preprocess_obj(input_path, output_path="processed_model.npz"):
    """Complete preprocessing pipeline."""
    verts, faces = load_obj(input_path)
    verts = normalize_vertices(verts)
    verts, faces = remove_duplicate_vertices(verts, faces)
    save_processed_data(verts, faces, output_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MixAR OBJ Preprocessing Tool")
    parser.add_argument("--input", type=str, required=False, default="airboat.obj",
                        help="Path to the input OBJ file (default: airboat.obj)")
    parser.add_argument("--output", type=str, required=False, default="processed_airboat.npz",
                        help="Output file name (.npz)")

    args = parser.parse_args()

    try:
        preprocess_obj(args.input, args.output)
        print("🎉 Preprocessing completed successfully.")
    except Exception as e:
        print(f"❌ Error during preprocessing: {e}")
