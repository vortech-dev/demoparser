import pandas as pd
from typing import Dict, Sequence, Optional, List, Tuple, Any

class DemoParser:
    def __init__(self, path: str) -> None: ...
    def parse_header(self) -> Dict[str, str]: ...
    def list_game_events(self) -> List[str]: ...
    def parse_grenades(self) -> pd.DataFrame: ...
    def parse_player_info(self) -> pd.DataFrame: ...
    def parse_item_drops(self) -> pd.DataFrame: ...
    def parse_skins(self) -> pd.DataFrame: ...
    def parse_event(
        self,
        event_name: str,
        player: Optional[Sequence[str]] = None,
        other: Optional[Sequence[str]] = None,
    ) -> pd.DataFrame: ...
    def parse_events(
        self,
        event_name: Sequence[str],
        player: Optional[Sequence[str]] = None,
        other: Optional[Sequence[str]] = None,
    ) -> List[Tuple[str, pd.DataFrame]]: ...
    def parse_voice(self) -> Dict[str, bytes]: ...
    def parse_ticks(
        self,
        wanted_props: Sequence[str],
        players: Optional[Sequence[int]] = None,
        ticks: Optional[Sequence[int]] = None,
    ) -> pd.DataFrame:
        """Parse the specified props.

        Args:
            wanted_props (Sequence[str]): The props to parse for each player at each tick.
            player (Optional[Sequence[int]]): Sequence of Steam IDs of the players to parse.
                `None` or an empty Sequence means all players. Defaults to `None`.
            ticks (Optional[Sequence[int]]): Sequence of ticks to parse.
                `None` or an empty Sequence means all ticks. Defaults to `None`.

        Returns:
            pd.DataFrame: Dataframe of all the parsed props for each player at each tick.
        """

    def parse_user_cmd(self) -> List[Dict[str, Any]]:
        """Parse user commands from the demo.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing user command data.
            Each dictionary includes:
            - entity_id: int
            - viewangle_x: float
            - viewangle_y: float
            - viewangle_z: float
            - buttonstate_1: int
            - buttonstate_2: int
            - buttonstate_3: int
            - forwardmove: float
            - leftmove: float
            - impulse: int
            - mouse_dx: int
            - mouse_dy: int
            - input_history: List[Dict[str, Any]]
        """
