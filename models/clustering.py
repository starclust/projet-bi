from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
import hdbscan

def scale_features(df):
    features = df[[
        "Amount_payement_Customer", 
        "Revenu_monoprix", 
        "Investissement_dans_les_Actifs"
    ]]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)
    return X_scaled

def apply_kmeans(df, X_scaled, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster_kmeans"] = kmeans.fit_predict(X_scaled)
    return df

def apply_dbscan(df, X_scaled):
    dbscan = DBSCAN(eps=0.7, min_samples=5)
    df["cluster_dbscan"] = dbscan.fit_predict(X_scaled)
    return df

def apply_hdbscan(df, X_scaled):
    hdb = hdbscan.HDBSCAN(min_cluster_size=5)
    df["cluster_hdbscan"] = hdb.fit_predict(X_scaled)
    return df

def apply_all_clusterings(df):
    X_scaled = scale_features(df)
    df = apply_kmeans(df, X_scaled)
    df = apply_dbscan(df, X_scaled)
    df = apply_hdbscan(df, X_scaled)
    return df
