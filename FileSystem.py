class Solution(object):
    def getLongestPath2(self, filesys):
        list = filesys.splitlines()  # Parse the string into list
        st = [0]  # to add the path separator before root dir
        lastLevel = -1  # depth of the last item in st
        sum = 0
        for item in list:
            print(item)
            bareName = item.lstrip(' ')  # Strip leading '\t's
            curLevel = len(item) - len(bareName) # Use number of '\t's to find level
            while (curLevel <= lastLevel):  # cd .. to the same level as "item"
                st.pop()
                lastLevel -= 1
            st.append(len(bareName) + st[-1] + 1)  # accumulated length, +1 for path-sep
            lastLevel = curLevel
            if ('.' in item):  # Only count "files" with an extension
                sum += st[-1]
            print("#", st, curLevel, sum)
        return sum

    def getLongestPath(self, S):
        list = S.splitlines()
        seperator_array = [0]
        last_level = -1
        maximum_length = 0
        for item in list:
            print(item)
            fs_name = item.lstrip(' ')
            current_level = len(item) - len(fs_name)
            while current_level <= last_level:
                seperator_array.pop()
                last_level -= 1
            seperator_array.append(len(fs_name) + seperator_array[-1] + 1)
            last_level = current_level
            if '.jpeg' in item or '.png' in item or '.gif' in item:
                maximum_length = max(maximum_length, seperator_array[-2])
            print("#", seperator_array, current_level, maximum_length)
        return maximum_length

mySol = Solution()
print(mySol.getLongestPath("d1\n d2\n  d4\nd3\n t.png\nd3\n t.png"))