class solution:
    def sortNutsandBolts(self,nuts,bolts,compare):
        if not nuts or not bolts or compare is None:
            return
        self.compare = compare
        self.quickSort(nuts,bolts,0,len(nuts)-1)

    def quickSort(self,nuts,bolts,left,right):
        if left >= right:
            return
        split_nut_pos = self.partition(nuts,bolts[left],left,right)
        self.partition(bolts,nuts[split_nut_pos],left,right)
        self.quickSort(nuts,bolts,left,split_nut_pos - 1)
        self.qucikSort(nuts,bolts,split_nut_pos + 1,right)


    def partition(self,items,pivot,left,right):
        if items == [] or pivot == None:
            return
        for i in range(left,right+1):
            if self.compare.cmp(pivot,items[i]) == 0 \
                or self.compare.cmp(items[i],pivot) == 0:
                items[left],items[i] = items[i],items[left]
                break
        pivot_partner = items[left]
        while left < right:
            while left < right and \
                    (self.compare.cmp(pivot,items[right]) == -1 \
                    or self.compare.cmp(items[right],pivot) == 1):
                right -= 1
            items[left] = items[right]
            while left < right and \
                    (self.compare.cmp(pivot,items[left]) == 1 \
                    or self.compare.cmp(items[left],pivot) == -1):
                left += 1
            items[right] = items[left]

        items[left] = pivot_partner
        return left


