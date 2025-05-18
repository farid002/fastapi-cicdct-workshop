from fastapi import APIRouter, HTTPException, Body

router = APIRouter()


@router.post("/prime")
def check_prime(number: int = Body(..., embed=True)):
    if number < 2:
        return {"result": "Sade ədəd yalnız 2 və daha böyük ədədlər ola bilər."}

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {"result": f"{number} sade ədəd deyil."}

    return {"result": f"{number} sade ədəddir."}
