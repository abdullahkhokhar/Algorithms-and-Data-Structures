class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # You could for each work create a new array in morse code
        # then compare each element with one another
        # would be time consuming

        # remember that a set does not contain duplicate values
        # so convert each word to morse and put it into the set
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
        ".---", "-.-",".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--","-..-", "-.--", "--.."]

        val_dict = dict() # MAKE A DICTINARY MAPING LETTER TO MORSE CODE
        ord_val = 97
        for i in codes:
            val_dict.update({chr(ord_val): i})
            ord_val += 1

        word_split = []
        final_list = set()
        for i in words:
            word_split.append(list(i)) # make each word a list and put it into word_split
        for x in word_split:
            result = ""
            for k in x:
                result += val_dict.get(k)
        final_list.add(result)
        #result_val = set(Counter(final_list).items())
        return len(result_val)
