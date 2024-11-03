# 6, 7, 10
from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.post("/validate_terraform")
def validateTerraform(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)
