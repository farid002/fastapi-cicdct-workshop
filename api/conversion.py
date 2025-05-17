from fastapi import APIRouter, HTTPException, Body

router = APIRouter()

@router.post("/convert")
def convert_units(
    value: float = Body(...),
    from_unit: str = Body(...),
    to_unit: str = Body(...)
):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        result = (value * 9 / 5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        result = (value - 32) * 5 / 9
    else:
        raise HTTPException(status_code=400, detail="Conversion not supported")

    return {"result": result}