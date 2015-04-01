#define BOOST_TEST_MODULE SCU
#include <boost/test/unit_test.hpp>

#include "dcmtkpp/SCU.h"

BOOST_AUTO_TEST_CASE(DefaultConstructor)
{
    dcmtkpp::SCU const scu;
    BOOST_CHECK_EQUAL(scu.get_affected_sop_class(), "");
}

BOOST_AUTO_TEST_CASE(AffectedSOPClassUID)
{
    dcmtkpp::SCU scu;
    scu.set_affected_sop_class("1.2.3");
    BOOST_CHECK_EQUAL(scu.get_affected_sop_class(), "1.2.3");
}
