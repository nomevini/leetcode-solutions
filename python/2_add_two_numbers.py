def addTwoNumbers(l1, l2):
    number01 = []
    number02 = []

    while l1:
        number01.append(l1.val)
        l1 = l1.next
    while l2:
        number02.append(l2.val)
        l2 = l2.next

    number01 = int(''.join([str(x) for x in number01[::-1]]))
    number02 = int(''.join([str(x) for x in number02[::-1]]))
    
    list_result = list(str(number01 + number02))

    # criar uma lista de list node sem fazer os nos
    nodes = []
    for number in list_result:
        nodes.append(ListNode(val=int(number)))

    # conectar os nos
    for index, node in enumerate(nodes):
        if index != 0:
            node.next = nodes[index - 1]
    
    return nodes[-1]
