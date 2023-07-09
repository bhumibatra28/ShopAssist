from joblib import load, dump

def modelSerializer(model: any, path: str, name: str):
    dump(value=model, filename=f"{path if path+'/' else ''}{name}")

def modelDeserializer(pathToFile: str):
    return load(pathToFile)