from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case "Player":
                return Player(entity_name, position)
        pass
