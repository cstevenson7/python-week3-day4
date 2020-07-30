class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

        
class LinkedList():
    def __init__(self):
        self.head = None
    
    #PUSHES TO THE FRONT
    def pushOn(self,new_value):
        new_node = Node(new_value) # new box in list, access to first node
        new_node.next = self.head
        self.head = new_node # now we have the beginning of the list with first value
        
    def insertAfter(self,prev_node, new_value):
        # check if the previous node even exists
        if prev_node is None:
            print("The given previous node, must not be empty")
            return
        # if node is not empty then create a new node
        new_node = Node(new_value)
                        
        #update the previous nodes next pointer to point to the next node's value) Keeping tarck of where you are
        # Dont want to lose Monday
        new_node.next = prev_node.next
                        
        #Update the previous node to point to the new nodes value-
        #this time we areteiilin the previous value to point to 
        prev_node.next = new_node
                        
     #This method will append a new node to the end of the linke dlist                        
    def append(self, new_value):
        #Create NewNode with a new value
        new_node = Node(new_value)
                        
        #check if the Linkedlist is empty
        #AND if it is , make THIS new node the head node( Beginning of the list)
                        
        if self.head is None:
            self.head = new_node

        #BUT if the list is not empty - traverse to the end
        #And add the NEW Value to the end of the list

        last = self.head # keeping track of where we are

        #While last.next is not none -> continue to loop until we find a None value
        while(last.next):
            last = last.next
            #Change current last node value to point to the new value
        last.next = new_node
                        
    # Now we need to traverse thru the likedlist
    def traverse(self):
        temp = self.head
        #While temp is not NONE -> keep looping through the list until yu reach a none valie
        while (temp):                        
            print(temp.value)
            temp = temp.next
                        
weekdays_links =  LinkedList()
#Insert a new day into the list
weekdays_links.pushOn('Mon')
weekdays_links.append("Tue")
weekdays_links.insertAfter(weekdays_links.head.next, 'Wed')
weekdays_links.append("Thu")
weekdays_links.traverse()