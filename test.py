from manim import *
from manim_slides import Slide

arr = [3,7,2,5,9]

class SelectionSort(Slide):
    def construct(self):
        title = Text("Selection Sort", color=WHITE)
        title.to_edge(UP+LEFT)
        self.play(Write(title))
        
        boxes = VGroup(*[BoxedNumber(i) for i in arr])
        boxes.arrange(RIGHT)

        compare = Vector(DOWN)
        compare.next_to(boxes[1], UP)

        lowest = Vector(DOWN, color=RED)
        lowest.next_to(boxes[0], UP)

        self.play(Create(boxes), Create(compare), Create(lowest))
        self.next_slide()

        for i in range(len(boxes)):
            min_idx = i
            self.play(lowest.animate.next_to(boxes[i], UP))
            self.next_slide()

            for j in range(i+1, len(boxes)):
                self.play(compare.animate.next_to(boxes[j], UP))
                self.next_slide()
                if boxes[min_idx].number > boxes[j].number:
                    min_idx = j
                    self.play(lowest.animate.next_to(boxes[j], UP))
                    self.next_slide()
                    
            # Swap the found minimum element with
            # the first element       
            boxes[i], boxes[min_idx] = boxes[min_idx], boxes[i]

            # boxes.sort(submob_func=lambda x: x.number)
            self.play(boxes.animate.arrange(RIGHT))
            self.next_slide()

            boxes[i].box.set_fill(GREEN, opacity=0.5)
        
        #self.next_slide()
        self.wait()

class InsertionSort(Slide):
    def construct(self):
        title = Text("Insertion Sort", color=WHITE)
        title.to_edge(UP+LEFT)
        self.play(Write(title))

        boxes = VGroup(*[BoxedNumber(i) for i in arr])
        boxes.arrange(RIGHT)
        boxes[0].box.set_fill(ORANGE, opacity=0.5)

        compare = Vector(DOWN)
        compare.next_to(boxes[0], UP)

        lowest = Vector(DOWN, color=RED)
        lowest.next_to(boxes[0], UP)

        self.play(Create(boxes), Create(compare), Create(lowest))
        self.next_slide()

        for i in range(1, len(boxes)):
            
            key = boxes[i]

            self.play(lowest.animate.next_to(boxes[i], UP))
            self.next_slide()

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key.number < boxes[j].number :
                    self.play(compare.animate.next_to(boxes[j], UP))
                    self.next_slide()
                    boxes[j + 1] = boxes[j]
                    j -= 1
                
            self.play(compare.animate.next_to(boxes[j+1], UP + LEFT))
            self.next_slide()
            boxes[j + 1] = key

            key.box.set_fill(ORANGE, opacity=0.5)
            self.play(boxes.animate.arrange(RIGHT))

        for box in boxes: box.box.set_fill(GREEN, opacity=0.5) 
        self.wait()

class BubbleSort(Slide):
    def construct(self):
        title = Text("Bubble Sort", color=WHITE)
        title.to_edge(UP+LEFT)
        self.play(Write(title))

        boxes = VGroup(*[BoxedNumber(i) for i in arr])
        boxes.arrange(RIGHT)

        compare = Vector(DOWN)
        compare.next_to(boxes[0], UP)

        lowest = Vector(DOWN, color=RED)
        lowest.next_to(boxes[0], UP)

        self.play(Create(boxes), Create(compare), Create(lowest))
        self.next_slide()

        n = len(boxes)
      
        # Traverse through all array elements
        for i in range(n):
            #self.play(lowest.animate.next_to(boxes[i], UP))
            #self.next_slide()
            swapped = False
    
            # Last i elements are already in place
            for j in range(0, n-i-1):
                self.play(lowest.animate.next_to(boxes[j], UP), compare.animate.next_to(boxes[j+1], UP))
                self.next_slide()

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if boxes[j].number > boxes[j+1].number:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
                    self.play(boxes.animate.arrange(RIGHT))
                    self.next_slide()

                    swapped = True
            boxes[n-i-1].box.set_fill(GREEN, opacity=0.5)
            
            # This a slight speedup as it would exit if it did not have to swap for a full cycle 
            # (meaning everything is already in the correct order)
            #if (swapped == False):
                #break

        self.wait()



class BoxedNumber(VGroup):
    def __init__(self, number, **kwargs):
        super().__init__(**kwargs)
        self.number = number

        self.box = Rectangle().scale(.5)
        self.add(self.box)

        self.text = Integer(number=self.number).move_to(self.box.get_center())
        self.add(self.text)