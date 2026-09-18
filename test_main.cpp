// #define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>
// #include "catch.hpp"
#include "UVSim.hpp"

using namespace std;

TEST_CASE("UVSim Branching Operations Work Correctly", "[branching]") {
    //set-up test variables
    int currentAddress = 10;
    int targetAddress = 45;
    int accumulator = 0;

    SECTION("Branch(40) always updates currentAddress") {
        bool result = branch(currentAddress, targetAddress);

        REQUIRE(result == true);
        REQUIRE(currentAddress == 45);
    }
    SECTION("Branch Neg (41) conditional checks") {
        SECTION("Does NOT branch when accumulator is positive") {
            accumulator = 100;
            bool result = branchneg(currentAddress, targetAddress, accumulator);

            REQUIRE(result == false);
            REQUIRE(currentAddress == 10); // Address should remain unchanged
        }

        SECTION("Branches when accumulator is negative") {
            accumulator = -50;
            bool result = branchneg(currentAddress, targetAddress, accumulator);

            REQUIRE(result == true);
            REQUIRE(currentAddress == 45); // Address should update to target
        }
    }

    SECTION("Branch Zero (42) conditional checks") {
        SECTION("Branches when accumulator is exactly zero") {
            accumulator = 0;
            bool result = branchzero(currentAddress, targetAddress, accumulator);

            REQUIRE(result == true);
            REQUIRE(currentAddress == 45); // Address should update to target
        }

        SECTION("Does NOT branch when accumulator is non-zero") {
            accumulator = 7;
            bool result = branchzero(currentAddress, targetAddress, accumulator);

            REQUIRE(result == false);
            REQUIRE(currentAddress == 10); // Address should remain unchanged
        }
    }
}

TEST_CASE("UVSim Arithmetic Operations Work Correctly", "[arithmetic]") {
    // Set up memory array
    string memory[100];
    for (int i = 0; i < 100; i++) {
        memory[i] = "+0000";
    }

    SECTION("Addition(30) Operation tests") {
        SECTION("Addition(30) adds memory value to accumulator") {
            memory[10] = "+0005";  // Put 5 in memory location 10
            int accumulator = 3;

            add(accumulator, memory, 10);

            REQUIRE(accumulator == 8);  // 3 + 5 = 8
        }
        SECTION("Addition(30) adds negative numbers") {
            memory[10] = "-0005";
            int accumulator = 3;

            add(accumulator, memory, 10);

            REQUIRE(accumulator == -2); // 3 + (-5) = -2
        }
    }


    SECTION("Subtraction(31) Operation tests") {
        SECTION("Subtraction(31) subtracts memory value from accumulator") {
            memory[10] = "+0003";  // Put 3 in memory location 10
            int accumulator = 10;

            subtract(accumulator, memory, 10);

            REQUIRE(accumulator == 7);  // 10 - 3 = 7
        }
        SECTION("Subtraction(31) subtracts negative numbers") {
            memory[10] = "-0003";
            int accumulator = -10;

            subtract(accumulator, memory, 10);

            REQUIRE(accumulator == -7); // -10 - (-3) = -10 + 3 = -7
        }
    }


    SECTION("Multiplication(33) operation tests") {
        SECTION("Multiplication(33) multiplies memory value by accumulator") {
            memory[10] = "+0004";  // Put 4 in memory location 10
            int accumulator = 5;

            multiply(accumulator, memory, 10);

            REQUIRE(accumulator == 20);  // 5 * 4 = 20
        }
        SECTION("Multiplication(33) by negative numbers") {
            memory[10] = "0004";
            int accumulator = -5;

            multiply(accumulator, memory, 10);

            REQUIRE(accumulator == -20);
        }
    }

    SECTION("Division(32) divides accumulator by memory value") {
        memory[10] = "+0005";  // Put 5 in memory location 10
        int accumulator = 20;

        divide(accumulator, memory, 10);

        REQUIRE(accumulator == 4);  // 20 / 5 = 4
    }

    SECTION("Division(32) handles divide by zero") {
        memory[10] = "+0000";  // Put 0 in memory location 10
        int accumulator = 10;

        int result = divide(accumulator, memory, 10);

        REQUIRE(result == -1);      // Should return error code
        REQUIRE(accumulator == 10); // Accumulator should remain unchanged
    }
}
