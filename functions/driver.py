def process_driver(exte, file):
    from functions.extension import ALLOWED_EXTENSIONS
    if exte in ALLOWED_EXTENSIONS[:3]:
        from modes.modeA import modeA
        return(modeA(exte, file))
    else:
        pass
