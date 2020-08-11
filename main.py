# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
import LRUCache_146

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('----------------------------------------------------')
    # test solution
    obj = LRUCache_146.LRUCache(2)
    obj.put(1, 1)
    print(obj.get(1))
