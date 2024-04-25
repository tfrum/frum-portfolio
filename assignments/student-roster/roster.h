#ifndef ROSTER_H
#define ROSTER_H

#include "student.h"

#include <array>
#include <string>


class Roster {
    private:
        // if we wanted to have more students or integrate a function that allocates
        // memory based on the input list size, it would be good to have this around
        static const int MAX_STUDENTS = 5;
        // here's out pointer array
        Student** classRosterArray;
        // presumably we wanto be able to handle less than the maximum amount of students without errors
        int lastIndex; 
        
    public:
        // default constructor
        Roster();
        // destructor
        ~Roster();

        //getter for classRosterArray
        Student** getClassRosterArray();


        // this is how we add students (), it calls add()
        void parseAndAddStudent(const std::string& studentData);
        //this is our adding function
        void add(const std::string& studentID,
                 const std::string& firstName,
                 const std::string& lastName,
                 const std::string& emailAddress,
                 int age,
                 std::array<int, 3> daysInCourse,
                 DegreeProgram degreeProgram);

        // a quick print function that prints using the student class print function
        void remove(const std::string& studentID);

        void printAverageDaysInCourse(const std::string& studentID) const;

        void printAll() const;
        
        void printInvalidEmails() const;

        void printByDegreeProgram(DegreeProgram degreeProgram) const;


};
#endif