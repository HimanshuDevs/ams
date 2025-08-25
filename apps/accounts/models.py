from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Date, func
from config.database import Base


class BaseModel(Base):
    __abstract__ = True
    is_active          = Column(Boolean, default=True, nullable=False)
    created_at         = Column(DateTime, nullable= False, default=func.now())
    updated_at         = Column(DateTime, nullable=True, onupdate=func.now())


class AuthUsers(BaseModel):
    __tablename__ = 'auth_users'
    id                 = Column(Integer, primary_key=True, index=True)
    type               = Column(String(150), nullable=True)
    full_name          = Column(String(150), nullable=False)
    username           = Column(String(50), nullable=False)
    email              = Column(String(50), nullable=False)
    password           = Column(String(255), nullable=False)

class DepartmentMaster(BaseModel):
    __tablename__ = "department_master"
    id                 = Column(Integer, primary_key=True)
    department_name    = Column(String(100), nullable=False)
    submitted_by       = Column(ForeignKey('auth_users.id', ondelete='RESTRICT'), nullable=True)

class CourseMaster(BaseModel):
    __tablename__ = "course_master"
    id                 = Column(Integer, primary_key=True)
    course_name        = Column(String(100), nullable=False)
    department_id      = Column(ForeignKey('department_master.id', ondelete='RESTRICT'), nullable=False)
    semester           = Column(String(50), nullable=True)
    classes            = Column(String(50), nullable=True)
    lecture_hours      = Column(Integer, nullable=True)
    submitted_by       = Column(ForeignKey('auth_users.id', ondelete='RESTRICT'), nullable=True)

class Student(BaseModel):
    __tablename__ = "students"
    id                 = Column(Integer, primary_key=True)
    full_name          = Column(String(150), nullable=False)
    department_id      = Column(ForeignKey('department_master.id', ondelete='RESTRICT'), nullable=False)
    classes            = Column(String(50), nullable=True)
    submitted_by       = Column(ForeignKey('auth_users.id', ondelete='RESTRICT'), nullable=True)

class AttendanceLog(BaseModel):
    __tablename__ = "attendance_log"
    id                 = Column(Integer, primary_key=True)
    student_id         = Column(ForeignKey('students.id', ondelete='RESTRICT'), nullable=True)
    course_id          = Column(ForeignKey('course_master.id', ondelete='RESTRICT'), nullable=True)
    present            = Column(Boolean, default=False)
    submitted_by       = Column(ForeignKey('auth_users.id', ondelete='RESTRICT'), nullable=True)