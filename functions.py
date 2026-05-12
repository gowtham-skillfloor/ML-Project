import joblib

def download_model(model):
    joblib_model = joblib.dump(model, "model.joblib")
    return joblib_model