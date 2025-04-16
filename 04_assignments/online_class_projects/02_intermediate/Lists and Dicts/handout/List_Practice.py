# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Length of fruit list:", len(fruit_list))
    fruit_list.append('mango')
    print("Updated fruit list:", fruit_list)
if __name__ == '__main__':
    main()