from code.Entity import Entity


class Meteor(Entity):
    def __init__(self, name, position, animations):
        super().__init__(name, position, animations)

        self.current_frame = 0
        self.image = self.animations["fall"][0]
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        self.rect.y += self.speed                

        # animação dos frames
        self.current_frame += (
            0.15  # mais devagar para ficar mais natural a transição dos frames
        )
        if self.current_frame >= len(self.animations["fall"]):
            self.current_frame = 0  # se chegar ao fim da lista volta para a primeira

        self.image = self.animations["fall"][int(self.current_frame)]

        self.rect = self.image.get_rect(
            center=self.rect.center
        )  # redesenha a box do frame
