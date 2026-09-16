#define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>
#include "UVSim.hpp"

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
