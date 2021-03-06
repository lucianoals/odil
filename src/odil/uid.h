/*************************************************************************
 * odil - Copyright (C) Universite de Strasbourg
 * Distributed under the terms of the CeCILL-B license, as published by
 * the CEA-CNRS-INRIA. Refer to the LICENSE file or to
 * http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
 * for details.
 ************************************************************************/

#ifndef _d8ae0008_075b_4a28_a241_1c6fb1a6c79b
#define _d8ae0008_075b_4a28_a241_1c6fb1a6c79b

#include <string>

#include "odil/odil.h"

namespace odil
{

/// @brief UID prefix of Odil.
std::string const uid_prefix="1.2.826.0.1.3680043.9.5560";

/// @brief Implementation class UID of Odil.
extern ODIL_API std::string implementation_class_uid;

/// @brief Implementation version name of Odil.
extern ODIL_API std::string implementation_version_name;

/// @brief Generate a UID under the UID prefix.
std::string ODIL_API generate_uid();

}

#endif // _d8ae0008_075b_4a28_a241_1c6fb1a6c79b
