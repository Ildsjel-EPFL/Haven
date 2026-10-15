from pydantic import BaseModel, Field

class Situation(BaseModel):
    """Represents the evaluation of a situation with various attributes indicating different types of emergencies and conflicts.
    
    Attributes:
        security_emergency (bool): Indicates if there is a security emergency.
        health_emergency (bool): Indicates if there is a health emergency.
        confilct (bool): Indicates if there is a conflict situation.
        physical_violence (bool): Indicates if there is a situation of physical violence.
        sexual_violence (bool): Indicates if there is a situation of sexual violence.
        psychological_violence (bool): Indicates if there is a situation of psychological violence.
        economical_violence (bool): Indicates if there is a situation of economical violence.
        residential_permit (bool): Indicates if there is a situation related to residential permits.
        children_involved (bool): Indicates if children are involved in the situation.
        forced_marriage (bool): Indicates if there is a situation of forced marriage.
    """
    security_emergency : bool = Field(description="Indicates if there is a security emergency.")
    health_emergency : bool = Field(description="Indicates if there is a health emergency.")
    confilct : bool = Field(description="Indicates if there is a conflict situation.")
    physical_violence : bool = Field(description="Indicates if there is a situation of physical violence.")
    sexual_violence : bool = Field(description="Indicates if there is a situation of sexual violence.")
    psychological_violence : bool = Field(description="Indicates if there is a situation of psychological violence.")
    economical_violence : bool = Field(description="Indicates if there is a situation of economical violence.")
    residential_permit : bool = Field(description="Indicates if there is a situation related to residential permits.")
    children_involved : bool = Field(description="Indicates if children are involved in the situation.")
    forced_marriage : bool = Field(description="Indicates if there is a situation of forced marriage.")