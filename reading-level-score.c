#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text2);
int count_sentences(string text3);

// Array of grade results
string the_grade[] = {"Before Grade 1", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12", "Grade 13", "Grade 14", "Grade 15"};

int main(void)
{
    // Gets imput text from user
    string imput_text = get_string("Text: ");

    // Calls funtions
    int t = count_letters(imput_text);
    int t2 = count_words(imput_text);
    int t3 = count_sentences(imput_text);

    // Calculate Coleman-Liau index
    float index = 0.0588 * (float)t / (float)t2 * 100 - 0.296 * (float)t3 / (float)t2 * 100 - 15.8;

    // Prints out reading level using an array
    int z = round(index);
    {
        if (round(index) >= 1 && round(index) <= 15)
        {
            printf("%s\n", the_grade[z]);
        }
        else if (round(index) > 15)
        {
            printf("Grade 16+\n");
        }
        else
        {
            printf("Before Grade 1\n");
        }
    }

}

// Count letters funtion
int count_letters(string text)
{
    int is_alpha = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            is_alpha++;
        }
    }

    return is_alpha;
}

// Count words function
int count_words(string text2)
{
    int is_white = 0;

    for (int i = 0, len = strlen(text2); i < len; i++)
    {
        if (isspace(text2[i]))
        {
            is_white++;
        }
    }

    return is_white + 1;
}

// Count sentences function
int count_sentences(string text3)
{
    int is_sent = 0;

    for (int i = 0, len = strlen(text3); i < len; i++)
    {
        if ((text3[i]) == 33 || (text3[i]) == 63 || (text3[i]) == 46)
        {
            is_sent++;
        }
    }

    return is_sent;
}


