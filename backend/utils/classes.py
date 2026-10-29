from pydantic import BaseModel, Field
from typing import List, Tuple, Dict, ClassVar

class Situation(BaseModel):
    """
    Represents the evaluation of a situation with various attributes indicating different types of emergencies and conflicts.
    
    Attributes:
        security_emergency (bool): Indicates if there is a security emergency.
        health_emergency (bool): Indicates if there is a health emergency.
        conflict (bool): Indicates if there is a conflict situation.
        physical_violence (bool): Indicates if there is a situation of physical violence.
        sexual_violence (bool): Indicates if there is a situation of sexual violence.
        psychological_violence (bool): Indicates if there is a situation of psychological violence.
        economical_violence (bool): Indicates if there is a situation of economical violence.
        residential_permit (bool): Indicates if there is a situation related to residential permits.
        children_involved (bool): Indicates if children are involved in the situation.
        forced_marriage (bool): Indicates if there is a situation of forced marriage.

        _VIOLENCE_MAP (ClassVar[dict[Tuple[bool, bool, bool, bool], str]]): A mapping of different violence combinations to their corresponding descriptions.
    """
    # security_emergency : bool = Field(description="Indicates if there is a security emergency.")
    # health_emergency : bool = Field(description="Indicates if there is a health emergency.")
    conflict : bool = Field(description="Indicates if there is a conflict situation.", default=False)
    physical_violence : bool = Field(description="Indicates if there is a situation of physical violence.", default=False)
    sexual_violence : bool = Field(description="Indicates if there is a situation of sexual violence.", default=False)
    psychological_violence : bool = Field(description="Indicates if there is a situation of psychological violence.", default=False)
    economical_violence : bool = Field(description="Indicates if there is a situation of economical violence.", default=False)
    residential_permit : bool = Field(description="Indicates if there is a situation related to residential permits.", default=False)
    children_involved : bool = Field(description="Indicates if children are involved in the situation.", default=False)
    forced_marriage : bool = Field(description="Indicates if there is a situation of forced marriage.", default=False)

    _VIOLENCE_MAP : ClassVar[Dict[Tuple[bool, bool, bool, bool], str]] = {
        (False, False, False, False): "None",
        (True, False, False, False): "PHY",
        (False, True, False, False): "SEX",
        (False, False, True, False): "PSY",
        (False, False, False, True): "ECO",
        (True, True, False, False): "PHY_SEX",
        (True, False, True, False): "PHY_PSY",
        (True, False, False, True): "PHY_ECO",
        (False, True, True, False): "SEX_PSY",
        (False, True, False, True): "SEX_ECO",
        (False, False, True, True): "PSY_ECO",
        (True, True, True, False): "PHY_SEX_PSY",
        (True, True, False, True): "PHY_SEX_ECO",
        (True, False, True, True): "PHY_PSY_ECO",
        (False, True, True, True): "SEX_PSY_ECO",
        (True, True, True, True): "PHY_SEX_PSY_ECO"
    }

    @property
    def violence_type(self) -> str:
        """
        Determines the type of violence based on the boolean attributes of the situation.
        
        Returns:
            str: A description of the type of violence present in the situation.
        """
        return self._VIOLENCE_MAP[(self.physical_violence, self.sexual_violence, self.psychological_violence, self.economical_violence)]

class Condition(BaseModel):
    """
    Represents the conditions that need to be checked in a situation, with boolean attributes indicating whether certain actions or interventions are required.
    
    Attributes:
        police (bool): Indicates if police intervention is required.
        pack_your_things (bool): Indicates if the person should pack their things.
        leave_home (bool): Indicates if the person should leave home.
        gather_docs (bool): Indicates if the person should gather documents.
        preserve_evidence (bool): Indicates if the person should preserve evidence.
        medical_report (bool): Indicates if a medical report is needed.
        counselling_support_group (bool): Indicates if the person needs counselling or support group.
        neighbour (bool): Indicates if the person should talk to a neighbour.
        lavi (bool): Indicates if the person should contact LAVI.
        fin_legal_psy_support (bool): Indicates if the person should seek financial, legal, or psychological support.
        assets_protection (bool): Indicates if the person should take measures for asset protection.
    """
    police : bool = Field(description="Indicates if police intervention is required.", default=False)
    pack_your_things : bool = Field(description="Indicates if the person should pack their things.", default=False)
    leave_home : bool = Field(description="Indicates if the person should leave home.", default=False)
    gather_docs : bool = Field(description="Indicates if the person should gather documents.", default=False)
    preserve_evidence : bool = Field(description="Indicates if the person should preserve evidence.", default=False)
    medical_report : bool = Field(description="Indicates if a medical report is needed.", default=False)
    counselling_support_group : bool = Field(description="Indicates if the person needs counselling or support group.", default=False)
    neighbour : bool = Field(description="Indicates if the person should talk to a neighbour.", default=False)
    lavi : bool = Field(description="Indicates if the person should contact LAVI.", default=False)
    fin_legal_psy_support : bool = Field(description="Indicates if the person should seek financial, legal, or psychological support.", default=False)
    assets_protection : bool = Field(description="Indicates if the person should take measures for asset protection.", default=False)

    @property
    def mask(self) -> List[bool]:
        return [
            self.police,
            self.pack_your_things,
            self.leave_home,
            self.gather_docs,
            self.preserve_evidence,
            self.medical_report,
            self.counselling_support_group,
            self.neighbour,
            self.lavi,
            self.fin_legal_psy_support,
            self.assets_protection
        ]

class ChatRequest(BaseModel):
    """
    Represents a request for a chat interaction, containing the message to be processed.

    Attributes:
        message (str): The message content to be processed in the chat interaction.
    """
    message: str


class ChatResponse(BaseModel):
    """
    Represents a response to a chat interaction, containing the generated response.

    Attributes:
        response (str): The generated response to the chat interaction.
    """
    response: str