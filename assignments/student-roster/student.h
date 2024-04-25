// I chose to do an integer array for the three course completion days
// since that will save lines of code later.

#ifndef STUDENT_H
#define STUDENT_H

#include "degree.h"

#include <string>
#include <array>

//class Student definition
class Student {
private:
    std::string     studentID;
    std::string     firstName;
    std::string     lastName;
    std::string     emailAddress;
    int             studentAge;
    std::array<int, 3> daysInCourse;
    DegreeProgram   degreeProgram;

public:
    //constructor definition
    Student(std::string     studentID,
            std::string     firstName,
            std::string     lastName,
            std::string     emailAddress,
            int             studentAge,
            std::array<int, 3> daysInCourse,
            DegreeProgram   degreeProgram);

    //getter function definitions
    std::string     getStudentID() const;
    std::string     getFirstName() const;
    std::string     getLastName() const;
    std::string     getEmailAddress() const;
    int             getStudentAge() const;
    std::array<int, 3> getDaysInCourse() const;
    DegreeProgram   getDegreeProgram() const;

    // setter function definitions
    void setStudentID      (const std::string& studentID);
    void setFirstName      (const std::string& firstName);
    void setLastName       (const std::string& lastName);
    void setEmailAddress   (const std::string& emailAddress);
    void setStudentAge     (int studentAge);
    void setDaysInCourse   (std::array<int, 3> daysInCourse);
    void setDegreeProgram  (DegreeProgram degreeProgram);

    // print function definition
    void print(const std::string& variableName) const;
};

#endif
