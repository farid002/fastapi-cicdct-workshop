import math
from fastapi import APIRouter, HTTPException, Body

router = APIRouter()

@router.post("/factorial")
def factorial(
    value: int = Body(...),
):
    return math.factorial(value)