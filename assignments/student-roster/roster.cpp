#include "roster.h"

#include <iostream>
#include <string>
#include <array>
#include <sstream>

// constructor: we assume we have no students and a maximum amount
Roster::Roster() {
    lastIndex = -1;
    classRosterArray = new Student*[MAX_STUDENTS];
}

// destructor
Roster::~Roster() {
    // we need to loop through the array deleting objects being pointed to
    for (int i = 0; i <= lastIndex; ++i) {
        delete classRosterArray[i];
    }
    // now we delete the array itself
    delete[] classRosterArray;
}

// getter for classRosterArray
Student** Roster::getClassRosterArray() {
    return classRosterArray;
}

void Roster::parseAndAddStudent(const std::string& studentData) {
    std::istringstream dataStream(studentData);
    std::string token;
    std::array<std::string, 9> studentInfo;
    int index = 0;

    while (std::getline(dataStream, token, ',')) {
        studentInfo[index++] = token;
    }

    std::string studentID             = studentInfo[0];
    std::string firstName             = studentInfo[1];
    std::string lastName              = studentInfo[2];
    std::string emailAddress          = studentInfo[3];
    int studentAge                    = std::stoi(studentInfo[4]);
    std::array<int, 3> daysInCourse;
    daysInCourse[0]                   = std::stoi(studentInfo[5]);
    daysInCourse[1]                   = std::stoi(studentInfo[6]);
    daysInCourse[2]                   = std::stoi(studentInfo[7]);

    DegreeProgram degreeProgram;
    if (studentInfo[8] == "SECURITY") {
        degreeProgram = DegreeProgram::SECURITY;
    } else if (studentInfo[8] == "NETWORK") {
        degreeProgram = DegreeProgram::NETWORK;
    } else {
        degreeProgram = DegreeProgram::SOFTWARE;
    }

    add(studentID,
        firstName,
        lastName,
        emailAddress,
        studentAge,
        daysInCourse,
        degreeProgram);
}

void Roster::add(const std::string& studentID,
                 const std::string& firstName,
                 const std::string& lastName,
                 const std::string& emailAddress,
                 int age,
                 std::array<int, 3> daysInCourse,
                 DegreeProgram degreeProgram) {
    Student* student = new Student(studentID, 
                                  firstName, 
                                  lastName, 
                                  emailAddress, 
                                  age, 
                                  daysInCourse, 
                                  degreeProgram);

    classRosterArray[++lastIndex] = student;
}

void Roster::remove(const std::string& studentID) {
    bool found = false;
    int foundIndex = -1;

    // we should walk through the array and find the student by id
    for (int i = 0; i <= lastIndex; ++i) {
        if (classRosterArray[i]->getStudentID() == studentID) {
            found = true;
            foundIndex = i;
            break;
        }
    }
    // if we find that student we'll delete it and then push the array entries down an index
    if (found) {
        delete classRosterArray[foundIndex];

        for (int i = foundIndex; i < lastIndex; ++i) {
            classRosterArray[i] = classRosterArray[i + 1];
        }

        // then we need lastIndex to be smaller so other code still works after
        --lastIndex;

        std::cout << "Student with ID " << studentID << " removed from roster." << std::endl;
    } else {
        std::cout << "Student with ID " << studentID << " was not found in the roster." << std::endl;
    }
}

void Roster::printAverageDaysInCourse(const std::string& studentID) const {
    bool found = false;
    int totalDays = 0;
    int numCourses = 3;

    // we'll iterate through and find a student with a matching ID
    for (int i = 0; i <= lastIndex; ++i) {
        if (classRosterArray[i]->getStudentID() == studentID) {
            found = true;
            std::array<int, 3> daysInCourse = classRosterArray[i]->getDaysInCourse();
            totalDays = daysInCourse[0] + daysInCourse[1] + daysInCourse[2];
            break;
        }
    }

    if (found) {
        double averageDays = static_cast<double>(totalDays) / numCourses;
        std::cout << "Student with ID " << studentID << " has an average of " << averageDays << std::endl;
    } else {
        std::cout << "Student with ID " << studentID << " not found." << std::endl;
    }
}

void Roster::printInvalidEmails() const {
    for (int i = 0; i <= lastIndex; ++i) {
        std::string emailAddress = classRosterArray[i]->getEmailAddress();
        if (emailAddress.find(' ')    != std::string::npos 
            || emailAddress.find('@') == std::string::npos 
            || emailAddress.find('.') == std::string::npos) {
            std::cout << "Student with ID \"" << classRosterArray[i]->getStudentID() 
            << "\" has an invalid email address: " << emailAddress << std::endl;
        }
    }
}

void Roster::printByDegreeProgram(DegreeProgram degreeProgram) const {
    for (int i = 0; i <= lastIndex; ++i) {
        if (classRosterArray[i]->getDegreeProgram() == degreeProgram) {
            // I am passing a blank string because of reasons explained in the function implementation
            classRosterArray[i]->print("");
        }
    }
}

// roster printAll. Passes empty string to student::print().
// this function was designed to have more functionality than is there at the moment
void Roster::printAll() const {
    for (int i = 0; i <= lastIndex; ++i) {
        // this passes a blank string because I designed the student::print() function
        // to be able to deliver atomic data, which we won't be doing
        classRosterArray[i]->print("");
    }
}