/*-----------------------------------------------------------------------------
Filename        : ossimImageWriterFactoryRegistry.i
Author          : Vipul Raheja
License         : See top level LICENSE.txt file.
Description     : Contains SWIG-Python of class ossimImageWriterFactoryRegistry 
-----------------------------------------------------------------------------*/

%module pyossim

%{

#include <ossim/base/ossimObjectFactory.h>
#include <ossim/imaging/ossimImageWriterFactoryBase.h>
#include <ossim/imaging/ossimImageWriterFactoryRegistry.h>
#include <ossim/base/ossimFactoryListInterface.h>
#include <vector>
#include <iosfwd>
#include <ossim/base/ossimCommon.h>

%}

/* Include the required header files */
%import "ossim/base/ossimConstants.h"

/* Handling ossimImageWriterFactoryRegistry Assignment operator */
%rename(__set__) ossimImageWriterFactoryRegistry::operator=;


/* Wrapping class ossimImageWriterFactoryRegistry */
class ossimImageWriterFactoryRegistry : public ossimObjectFactory,
        public ossimFactoryListInterface<ossimImageWriterFactoryBase, ossimImageFileWriter>

{
        public:
                static ossimImageWriterFactoryRegistry* instance();

                ossimImageFileWriter *createWriter(const ossimFilename& filename)const;
                ossimImageFileWriter *createWriterFromExtension(const ossimString& fileExtension)const;
                ossimImageFileWriter *createWriter(const ossimKeywordlist &kwl,
                                const char *prefix=0)const;
                ossimImageFileWriter* createWriter(const ossimString& typeName)const;

                ossimObject* createObject(const ossimKeywordlist &kwl,
                                const char *prefix=0)const
                {
                        return createObjectFromRegistry(kwl, prefix);
                }
                ossimObject* createObject(const ossimString& typeName)const
                {
                        return createObjectFromRegistry(typeName);
                }

                /**
                 * getTypeNameList.  This should return the class type of the object being
                 * used to perform the writting.
                 */
                virtual void getTypeNameList(std::vector<ossimString>& typeList)const
                {
                        getAllTypeNamesFromRegistry(typeList);
                }

                /**
                 * getImageTypeList.  This is the actual image type name.  So for
                 * example, ossimTiffWriter has several image types.  Some of these
                 * include TIFF_TILED, TIFF_TILED_BAND_SEPARATE ... etc.
                 * The ossimGdalWriter
                 * may include GDAL_IMAGINE_HFA, GDAL_RGB_NITF, GDAL_JPEG20000, ... etc
                 * A writer should be able to be instantiated by this name as well as a
                 * class name
                 */
                virtual void getImageTypeList(std::vector<ossimString>& imageTypeList)const;

                virtual void getImageFileWritersBySuffix(ossimImageWriterFactoryBase::ImageFileWriterList& result,
                                const ossimString& ext)const;
                virtual void getImageFileWritersByMimeType(ossimImageWriterFactoryBase::ImageFileWriterList& result,
                                const ossimString& mimeType)const;
                /**
                 * @brief Prints list of writers from getImageTypeList.
                 * @param  out Stream to print to.
                 * @return std::ostream&
                 */
                std::ostream& printImageTypeList(std::ostream& out)const;

                /**
                 * @brief Prints list of writers from getImageTypeList.
                 * @param  out Stream to print to.
                 * @return std::ostream&
                 */
                std::ostream& printWriterProps(std::ostream& out)const;

        protected:
                ossimImageWriterFactoryRegistry();
                ossimImageWriterFactoryRegistry(const ossimImageWriterFactoryRegistry&);
                void operator=(const ossimImageWriterFactoryRegistry&);

                static ossimImageWriterFactoryRegistry*    theInstance;
};

extern "C"
{
        OSSIMDLLEXPORT void* ossimImageWriterFactoryRegistryGetInstance();
}
