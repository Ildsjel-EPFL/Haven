from pydantic import BaseModel, Field
from typing import ClassVar, Dict, List, Tuple

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
    conflict : bool | None = Field(description="Indicates if there is a conflict situation. Use null when unknown.", default=None)
    physical_violence : bool | None = Field(description="Indicates physical violence. Use null when unknown.", default=None)
    sexual_violence : bool | None = Field(description="Indicates sexual violence. Use null when unknown.", default=None)
    psychological_violence : bool | None = Field(description="Indicates psychological violence. Use null when unknown.", default=None)
    economical_violence : bool | None = Field(description="Indicates economic violence. Use null when unknown.", default=None)
    residential_permit : bool | None = Field(description="Indicates a residential permit issue. Use null when unknown.", default=None)
    children_involved : bool | None = Field(description="Indicates whether children are involved. Use null when unknown.", default=None)
    forced_marriage : bool | None = Field(description="Indicates forced marriage. Use null when unknown.", default=None)
    needs_clarification : bool = Field(description="Indicates whether more information is required.", default=False)
    clarification_reason : str | None = Field(description="Explains which information is missing or ambiguous.", default=None)


    _VIOLENCE_MAP : ClassVar[Dict[Tuple[bool, bool, bool, bool], List[str]]] = {
        (False, False, False, False): ["CON"],
        (True, False, False, False): ["PHY"],
        (False, True, False, False): ["SEX"],
        (False, False, True, False): ["PSY"],
        (False, False, False, True): ["ECO"],
        (True, True, False, False): ["PHY", "SEX"],
        (True, False, True, False): ["PHY", "PSY"],
        (True, False, False, True): ["PHY", "ECO"],
        (False, True, True, False): ["SEX", "PSY"],
        (False, True, False, True): ["SEX", "ECO"],
        (False, False, True, True): ["PSY", "ECO"],
        (True, True, True, False): ["PHY", "SEX", "PSY"],
        (True, True, False, True): ["PHY", "SEX", "ECO"],
        (True, False, True, True): ["PHY", "PSY", "ECO"],
        (False, True, True, True): ["SEX", "PSY", "ECO"],
        (True, True, True, True): ["PHY", "SEX", "PSY", "ECO"]
    }

    @property
    def violence_types(self) -> List[str]:
        """
        Determines the type of violence based on the boolean attributes of the situation.
        
        Returns:
            List[str]: A list of strings describing the type of violence present in the situation.
        """
        return [
            violence
            for enabled, violence in zip(
                (
                    self.physical_violence,
                    self.sexual_violence,
                    self.psychological_violence,
                    self.economical_violence,
                ),
                ("PHY", "SEX", "PSY", "ECO"),
            )
            if enabled is True
        ]

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
        humiliation_recognition (bool): Indicates if the person should recognize humiliations and devaluations.
        doubt_recognition (bool): Indicates if the person should recognize when the other makes them doubt their experiences.
        responsibility_recognition (bool): Indicates if the person should recognize when the other makes them responsible for their behaviors.
        isolation_support (bool): Indicates if the person should seek support to overcome isolation.
        daily_control_recognition (bool): Indicates if the person should recognize control over their daily life.
        digital_privacy_protection (bool): Indicates if the person should protect their digital exchanges and privacy.
        intimidation_threats_handling (bool): Indicates if the person should handle intimidation and threats.
        children_threats_handling (bool): Indicates if the person should handle threats concerning children.
        harassment_handling (bool): Indicates if the person should handle harassment and imposed contacts.
        self_harm_threats_handling (bool): Indicates if the person should handle threats of self-harm or suicide from the other.
        private_informations_revelation_threats_handling (bool): Indicates if the person should handle threats of private information being revealed.
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
    humiliation_recognition : bool = Field(description="Indicates if the person should recognize humiliations and devaluations.", default=False)
    doubt_recognition : bool = Field(description="Indicates if the person should recognize when the other makes them doubt their experiences.", default=False)
    responsibility_recognition : bool = Field(description="Indicates if the person should recognize when the other makes them responsible for their behaviors.", default=False)
    isolation_support : bool = Field(description="Indicates if the person should seek support to overcome isolation.", default=False)
    daily_control_recognition : bool = Field(description="Indicates if the person should recognize control over their daily life.", default=False)
    digital_privacy_protection : bool = Field(description="Indicates if the person should protect their digital exchanges and privacy.", default=False)
    intimidation_threats_handling : bool = Field(description="Indicates if the person should handle intimidation and threats.", default=False)
    children_threats_handling : bool = Field(description="Indicates if the person should handle threats concerning children.", default=False)
    harassment_handling : bool = Field(description="Indicates if the person should handle harassment and imposed contacts.", default=False)
    self_harm_threats_handling : bool = Field(description="Indicates if the person should handle threats of self-harm or suicide from the other.", default=False)
    private_informations_revelation_threats_handling : bool = Field(description="Indicates if the person should handle threats of private information being revealed.", default=False)

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
            self.assets_protection,
            self.humiliation_recognition,
            self.doubt_recognition,
            self.responsibility_recognition,
            self.isolation_support,
            self.daily_control_recognition,
            self.digital_privacy_protection,
            self.intimidation_threats_handling,
            self.children_threats_handling,
            self.harassment_handling,
            self.self_harm_threats_handling,
            self.private_informations_revelation_threats_handling,
            ]

class ChatRequest(BaseModel):
    """
    Represents a request for a chat interaction, containing the message to be processed.

    Attributes:
        message (str): The message content to be processed in the chat interaction.
    """
    message: str
    language: str = "fr"
    session_id: str


class ChatResponse(BaseModel):
    """
    Represents a response to a chat interaction, containing the generated response.

    Attributes:
        response (str): The generated response to the chat interaction.
    """
    response: str