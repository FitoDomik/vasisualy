from ..core import speak
from ru_word2number import w2n
import random
trigger = ("Число от ", "число от ")
answer = ("Это ", "Ответ ", "Это число ")
def main(say, widget):
    for i in trigger:
        if i in say:
            nums = []
            for word in say.split():
                try:
                    num = w2n.word_to_num(word)  
                    nums.append(num)
                except ValueError:
                    pass
            while len(nums) > 2:
                nums.pop()  
            if len(nums) == 1:
                toSpeak = "Мне нужно второе число!"
                break
            elif len(nums) == 0:
                toSpeak = "Мне нужны два числа!"
                break
            num1 = int(nums[0])
            num2 = int(nums[1])
            randnum = random.randint(num1, num2)  
            toSpeak = random.choice(answer) + str(randnum) + "."
            break
        else:
            toSpeak = ""
    if toSpeak:
        speak.speak(toSpeak, widget)
    return toSpeak