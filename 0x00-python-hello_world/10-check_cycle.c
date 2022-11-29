#include "lists.h"
/**
 * check_cycle - this checks the linked list for circle
 * @list: this is a pointer to the head of the list
 * Return: returns 1 if there is a circle and returns 0 for false
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;

	while (head != NULL)
	{
		head = head->next;
		if (head == list)
		{
			return (1);
		}
	}
	return (0);
}
