#ifndef OBJECT_H
#define OBJECT_H

namespace me
{
    class Object
    {
        public:
            /** Default constructor */
            Object();
            /** Default destructor */
            virtual ~Object();
            void Draw();
        protected:
        private:
    };
};

#endif // OBJECT_H
