import numpy as np
import pandas as pd
import scipy.sparse as sp
import networkx as nx
import matplotlib.pyplot as plt

from pathlib import Path

# Directory with HetMat archive - change to match your path if does not already
DATA_DIR = Path("hetionet-v1.0.hetmat")

NODE_DIR = DATA_DIR / "nodes"
EDGE_DIR = DATA_DIR / "edges"

# Load node tables
diseases = pd.read_csv(NODE_DIR / "Disease.tsv", sep="\t")
genes = pd.read_csv(NODE_DIR / "Gene.tsv", sep="\t")
symptoms = pd.read_csv(NODE_DIR / "Symptom.tsv", sep="\t")

# Load sparse adjacency matrices
DaG = sp.load_npz(EDGE_DIR / "DaG.sparse.npz")  # Disease-associates-Gene
DpS = sp.load_npz(EDGE_DIR / "DpS.sparse.npz")  # Disease-presents-Symptom

print("Disease nodes:", len(diseases))
print("Gene nodes:", len(genes))
print("Symptom nodes:", len(symptoms))

print("\nDisease-Gene matrix:", DaG.shape)
print("Disease-Symptom matrix:", DpS.shape)

# Basic statistics function
def matrix_statistics(M, label):
    n_diseases, n_features = M.shape
    total_edges = M.nnz                 # num of nonzero entries

    # num of associations (edges) per disease
    disease_degrees = np.asarray(M.sum(axis=1)).flatten()

    # num of diseases associated with each gene/symptom
    feature_degrees = np.asarray(M.sum(axis=0)).flatten()

    print("\n", label)
    print("Diseases:", n_diseases)
    print("Features:", n_features)
    print("Total associations/edges:", total_edges)

    print("Associations per disease:")
    print("Mean:", np.mean(disease_degrees))
    print("Median:", np.median(disease_degrees))
    print("Standard deviation:", np.std(disease_degrees))
    print("Minimum:", np.min(disease_degrees))
    print("Maximum:", np.max(disease_degrees))

    print("Associations per feature:")
    print("Mean:", np.mean(feature_degrees))
    print("Median:", np.median(feature_degrees))
    print("Maximum:", np.max(feature_degrees))

    return disease_degrees, feature_degrees

# Basic statistics
DaG_disease_degree, DaG_gene_degree = matrix_statistics(DaG, "Disease-Gene Associations")
DpS_disease_degree, DpS_symptom_degree = matrix_statistics(DpS, "Disease-Symptom Associations")

# Degree distribution plots
plt.figure(figsize=(8, 5))
plt.hist(DaG_disease_degree, bins=50)
plt.xlabel("Number of associated genes")
plt.ylabel("Number of diseases")
plt.title("Disease-Gene Degree Distribution")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(DpS_disease_degree, bins=50)
plt.xlabel("Number of associated symptoms")
plt.ylabel("Number of diseases")
plt.title("Disease-Symptom Degree Distribution")
plt.show()