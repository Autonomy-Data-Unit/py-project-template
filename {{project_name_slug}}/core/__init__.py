import os, pkgutil, importlib, sys

def run_all():
    # Run all scripts in this folder in alphanumerical order
    scripts = list(f"{__package__}.{module_name}" for _, module_name, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))
    scripts = sorted(scripts)
    for s in scripts:
        print(f"{'#' * (len(s)+4)}")
        print(f"# {s} #")
        print(f"{'#' * (len(s)+4)}")
        if s in sys.modules:
            module = importlib.import_module(s)
            importlib.reload(module)
        else:
            importlib.import_module(s)