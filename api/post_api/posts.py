from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.userservice import *
from datetime import datetime
from typing import Optional
from database import get_db
from database.models import User