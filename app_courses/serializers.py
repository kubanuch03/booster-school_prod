from rest_framework import serializers,generics

from .models import (
    CourseTeacher,
    CourseDirection,
    Course,
    MajorBenefit,
    EducationBenefit,
    CourseProgram,
    TopicProgram,
    TeacherTechnology,
    AboutProfession,
    ClassesGoing,
    ClassGoingTopik

)

#===   Teacher ===================================================================================================================================

class TeacherTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTechnology
        fields = ['id','title','direction']


class CourseTeacherSerializer(serializers.ModelSerializer):
    technology = TeacherTechnologySerializer(many=True)

    class Meta:
        model = CourseTeacher
        fields = ['id','first_name','last_name','description','image','technology']

    def to_representation(self, instance):
        data_course = super().to_representation(instance)      
          
        data_course['technology'] = TeacherTechnologySerializer(instance.technology.all(),many=True).data
        
        return data_course




#===   Direction ===================================================================================================================================


class CourseDirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDirection
        fields = ['id','title']



#===   Major Benefit  ===================================================================================================================================


class MajorBenefitSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source='course.title')
    class Meta:
        model = MajorBenefit
        fields = ['id','title','image',]

#===   Education Benefit ===================================================================================================================================


class EducationBenefitSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source='course.title')
    class Meta:
        model = EducationBenefit
        fields = ['id','title','image',]


#===   About Profession ===================================================================================================================================

class AboutProfessionSerializer(serializers.ModelSerializer):
    major_benefit = MajorBenefitSerializer(many=True)
    major_education = EducationBenefitSerializer(many=True)
    class Meta:
        model = AboutProfession
        fields = ['id','title','description','image','major_benefit','major_education']




#===   Course Program ===================================================================================================================================

class TopicProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = TopicProgram
        fields = ['id','title',]

class CourseProgramSerializer(serializers.ModelSerializer):
    topic = TopicProgramSerializer(many=True)
    
    class Meta:
        model = CourseProgram
        fields = ['id', 'title', 'topic', 'course_direction']
    
    def to_representation(self, instance):
        data_course = super().to_representation(instance)
               
        data_course['topic'] = TopicProgramSerializer(instance.topic.all(), many=True).data
        
        return data_course

#===   Course ===================================================================================================================================



class CourseListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id','title','description','image','extended_image','duration','monthly_price',
                  'installment_price','lesson_duration','start_date','timetable',
                  'free_spots','direction','teacher','about_profession','course_program','discount',
                  ]


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = CourseTeacherSerializer()
    about_profession = AboutProfessionSerializer()
    direction = CourseDirectionSerializer()
    course_program = CourseProgramSerializer(many=True)
    education_benefit = EducationBenefitSerializer(many=True)
    major_benefit = MajorBenefitSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id','title','description','image','extended_image','duration','monthly_price',
                  'installment_price','lesson_duration','start_date','timetable',
                  'free_spots','direction','teacher','about_profession','course_program',
                  'education_benefit','major_benefit','discount'
                  ]
    def to_representation(self, instance):
        data_course = super().to_representation(instance)
               
        data_course['direction'] = CourseDirectionSerializer(instance.direction).data
        data_course['teacher'] = CourseTeacherSerializer(instance.teacher).data
        data_course['course_program'] = CourseProgramSerializer(instance.course_program.all(),many=True).data
        data_course['about_profession']={
            'id': data_course['about_profession']['id'],
            'title': data_course['about_profession']['title'],
            'course_direction': data_course['course_program'][0]['course_direction']
        }
        data_course['education_benefit'] = EducationBenefitSerializer(instance.about_profession.major_education.all(), many=True).data
        data_course['major_benefit'] = MajorBenefitSerializer(instance.about_profession.major_benefit.all(), many=True).data
        
        return data_course




#===   Class Going    ===================================================================================================================================




class ClassGoingTopikSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassGoingTopik
        fields = ['title','description','image','course',]



class ClassGoingSerializer(serializers.ModelSerializer):
    topik = ClassGoingTopikSerializer(many=True)

    class Meta:
        model = ClassesGoing
        fields = ['title','description','topik',]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['topik'] = ClassGoingTopikSerializer(instance.topik.all(), many=True).data


        return data