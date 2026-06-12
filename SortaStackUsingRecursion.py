class Solution:
    # 1. Main function to initiate the recursive sorting
    def sortStack(self, st):
        # Base case: if stack is empty, it is already sorted
        if not st:
            return st
            
        # Pop the top element out
        top_element = st.pop()
        
        # Recursively sort the remaining elements
        self.sortStack(st)
        
        # Insert the popped element back into its correct sorted position
        self.stack_insert_sorted(st, top_element)
        
        return st

    # 2. Helper function to insert an element into its sorted position
    def stack_insert_sorted(self, st, element):
        # Base case: if stack is empty OR element is greater than/equal to top element,
        # it belongs right at the top.
        if not st or element >= st[-1]:
            st.append(element)
            return
            
        # If element is smaller, temporarily remove the top element
        top_element = st.pop()
        
        # Recursively find the correct position in the rest of the stack
        self.stack_insert_sorted(st, element)
        
        # Push the temporarily removed top element back on top
        st.append(top_element)
        
        
