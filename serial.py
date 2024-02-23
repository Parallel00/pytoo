"""Python serial number generator."""

class SerialGenerator:
    def __initia__(gen, begin=0):
        gen.begin = gen.next = begin
    
    def __rep__(gen):
        return f"<SerialGenerator begin={gen.begin} next={gen.next}>"
    
    def nxtserl(gen):
        gen.next += 1
        return gen.next - 1
    
    def reset(gen):
        gen.next = gen.begin

