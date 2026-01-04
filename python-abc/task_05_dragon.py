#!/usr/bin/env python3
"""Task 5: The Mystical Dragon - Mastering Mixins"""

class SwimMixin:
    """Mixin class providing swimming capability"""
    
    def swim(self):
        """Print swimming message"""
        print("The creature swims!")

class FlyMixin:
    """Mixin class providing flying capability"""
    
    def fly(self):
        """Print flying message"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swimming and flying capabilities"""
    
    def roar(self):
        """Print dragon's roar"""
        print("The dragon roars!")


if __name__ == "__main__":
    # Demonstration when run directly
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
