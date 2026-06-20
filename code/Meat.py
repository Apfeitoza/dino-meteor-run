from code.Entity import Entity


class Meat(Entity):
    def __init__(self, name, position, animations):
        super().__init__(name, position, animations)

        self.image = self.animations
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        #não tem animação, ele só cai de acordo com a velocidade da const
        self.rect.y += self.speed
