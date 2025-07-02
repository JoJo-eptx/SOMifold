# Geometry-Aware High Injury Network Mapping with SOMifold

This project introduces a novel method for identifying **High Injury Networks (HINs)** by combining:

- **Self-Organizing Maps (SOMs)**
- **Graph geometry and curvature analysis**
- **Monetary weighting of crash severity**

Unlike traditional methods (e.g., KDE or crash counts), this approach models **spatial risk** as **deformation in a hexagonal SOM lattice**, capturing how crash severity reshapes local geometry.

---

## Installation

To install the package locally, clone or download this repository and run the following command from the project root directory:

```powershell
pip install .
```

For development (editable) mode, use:

```powershell
pip install -e .
```

## 🧠 Key Features

- **Hexagonal SOM Training:** One per severity class (Minor, Serious, Fatal)
- **Graph-Based Curvature:** Laplacian and tangent vectors capture spatial strain
- **Monetary Weighting:** Severity is scaled by societal cost:
  - Minor: $246,900
  - Serious: $1,254,700
  - Fatal: $132,000,000
- **Interpolated Risk Surface:** Combined into a continuous severity-aware field
- **GIS Integration:** Exported for visualization and routing in ArcGIS

---

## 🚦 Risk-Aware Routing

Road segments are treated as paths through a latent risk field. By integrating risk along each path, the framework enables:

- **Risk-aware shortest paths**
- **Hazard corridor detection**
- **Trade-off analysis between safety and efficiency**

---

## 🎯 Why Use This?

- Captures **topological deformation**, not just density
- Integrates **severity weighting** using real-world economic cost
- Produces **interpretable, GIS-ready** maps
- Enables **data-driven safety planning** at the network level

---

## 📍 Output

- Interpolated risk surface (.tif or feature layer for ArcGIS)
- Weighted SOM-based graphs (.gpickle)
- Risk-aware road network for routing analysis

---

## 📌 Citation

If you use this method in academic or policy work, please cite the original SOMifold research or acknowledge this framework in your materials.
- Castro II, Joel Gerardo. High Injury Network Mapping using Geometry-Aware Self-Organizing Maps. 2025.
