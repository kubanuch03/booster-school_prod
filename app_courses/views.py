from rest_framework import permissions, generics
from drf_spectacular.utils import extend_schema

from django.db.models import Prefetch

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

from .serializers import (
    CourseTeacherSerializer,
    CourseDirectionSerializer,
    CourseListSerializer,
    CourseDetailSerializer,
    MajorBenefitSerializer,
    EducationBenefitSerializer,
    CourseProgramSerializer,
    TopicProgramSerializer,
    TeacherTechnologySerializer,
    AboutProfessionSerializer,
    ClassGoingTopikSerializer,
    ClassGoingSerializer
)


#== Course Teacher ================================================================
class CourseTeacherListApiView(generics.ListAPIView):
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer

    @extend_schema(
        summary="Все Преподователи",
        description=" Запрос на Все Преподователей ",
        responses={200: CourseTeacherSerializer(many=True)},
        operation_id="list_course_teacher",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CourseTeacherDetailApiView(generics.RetrieveAPIView):
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer

    @extend_schema(
        summary="Детальная информация о  Преподователе",
        description="Детальная информация о  Преподователе",
        responses={200: CourseTeacherSerializer()},
        operation_id="detail_course_teacher",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#== Course Direction ================================================================

class CourseDirectionListApiView(generics.ListAPIView):
    queryset = CourseDirection.objects.all()
    serializer_class = CourseDirectionSerializer

    @extend_schema(
        summary="Все Курсы направления",
        description=" Запрос на Все курсы направления ",
        responses={200: CourseDirectionSerializer(many=True)},
        operation_id="list_course_direction",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseDirectionDetailApiView(generics.RetrieveAPIView):
    queryset = CourseDirection.objects.all()
    serializer_class = CourseDirectionSerializer

    @extend_schema(
        summary="Детальная информация о курс Направления",
        description="Детальная информация о  курс Направления",
        responses={200: CourseDirectionSerializer()},
        operation_id="detail_course_direction",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#== Course  ================================================================


class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

    def get_queryset(self):
        queryset = Course.objects.select_related('direction','teacher').all()
        return queryset

    @extend_schema(
        summary="Все Курсы ",
        description=" Запрос на Все Курсы  ",
        responses={200: CourseListSerializer(many=True)},
        operation_id="list_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

    @extend_schema(
        summary="Детальная информация о курсе",
        description="Детальная информация о  курсе",
        responses={200: CourseDetailSerializer()},
        operation_id="detail_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#== About Profession  ================================================================
class AboutProfessionListApiView(generics.ListAPIView):
    queryset = AboutProfession.objects.all()
    serializer_class = AboutProfessionSerializer

    

    @extend_schema(
        summary="Все   О Профессии",
        description=" Запрос на О Профессии",
        responses={200: AboutProfessionSerializer(many=True)},
        operation_id="list_about_profession",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class AboutProfessionDetailApiView(generics.RetrieveAPIView):
    queryset = AboutProfession.objects.all()
    serializer_class = AboutProfessionSerializer

    

    @extend_schema(
        summary="О Профессии",
        description="О Профессии",
        responses={200: AboutProfessionSerializer(many=True)},
        operation_id="list_about_profession",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
#== Major Benefit ================================================================

class MajorBenefitListApiView(generics.ListAPIView):
    queryset = MajorBenefit.objects.all()
    serializer_class = MajorBenefitSerializer

    def get_queryset(self):
        queryset = MajorBenefit.objects.all()
        return queryset

    @extend_schema(
        summary="Все Плюсы профессии ",
        responses={200: MajorBenefitSerializer(many=True)},
        operation_id="list_major_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MajorBenefitDetailApiView(generics.RetrieveAPIView):
    queryset = MajorBenefit.objects.all()
    serializer_class = MajorBenefitSerializer

    @extend_schema(
        summary="Детальная информация о о плюс профессии",
        description="Детальная информация о плюс профессии",
        responses={200: MajorBenefitSerializer()},
        operation_id="detail_major_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#== Education Benefit ================================================================


class EducationBenefitListApiView(generics.ListAPIView):
    queryset = EducationBenefit.objects.all()
    serializer_class = EducationBenefitSerializer

    def get_queryset(self):
        queryset = EducationBenefit.objects.all()
        return queryset

    @extend_schema(
        summary="Все Плюсы курса ",
        description=" Запрос на Все Плюсы Курсы  ",
        responses={200: CourseTeacherSerializer(many=True)},
        operation_id="list_education_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EducationBenefitDetailApiView(generics.RetrieveAPIView):
    queryset = EducationBenefit.objects.all()
    serializer_class = EducationBenefitSerializer

    @extend_schema(
        summary="Детальная информация о о плюс курса",
        description="Детальная информация о плюс курса",
        responses={200: EducationBenefitSerializer()},
        operation_id="detail_education_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#== Course Program ================================================================


class CourseProgramListApiView(generics.ListAPIView):
    queryset = CourseProgram.objects.all()
    serializer_class = CourseProgramSerializer

    def get_queryset(self):
        queryset = CourseProgram.objects.select_related('course_direction')
        return queryset

    @extend_schema(
        summary="Все Программа Курса ",
        description=" Запрос на Все Программа Курса  ",
        responses={200: CourseProgramSerializer(many=True)},
        operation_id="list_block_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseProgramDetailApiView(generics.RetrieveAPIView):
    queryset = CourseProgram.objects.all()
    serializer_class = CourseProgramSerializer

    @extend_schema(
        summary="Детальная информация Блок Курса",
        description="Детальная информация Блок Курса",
        responses={200: CourseProgramSerializer()},
        operation_id="detail_sub_block_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#== Block Subhead ================================================================


class TopicProgramListApiView(generics.ListAPIView):
    queryset = TopicProgram.objects.all()
    serializer_class = TopicProgramSerializer

    @extend_schema(
        summary="Все Под Блок Курса ",
        description=" Запрос на Все Под Блок Курса  ",
        responses={200: TopicProgramSerializer(many=True)},
        operation_id="list_sub_block_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TopicProgramDetailApiView(generics.RetrieveAPIView):
    queryset = TopicProgram.objects.all()
    serializer_class = TopicProgramSerializer

    @extend_schema(
        summary="Детальная информация Под Блок Курса",
        description="Детальная информация Под Блок Курса",
        responses={200: TopicProgramSerializer()},
        operation_id="detail_sub_block_course_get",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
#== Teacher Technology ================================================================


class TeacherTechnologyListApiView(generics.ListAPIView):
    queryset = TeacherTechnology.objects.all()
    serializer_class = TeacherTechnologySerializer

    @extend_schema(
        summary="Все Технологии Проподователей ",
        description=" Запрос на Все Технологии Проподователей ",
        responses={200: TeacherTechnologySerializer(many=True)},
        operation_id="list_teacher_technology_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TeacherTechnologyDetailApiView(generics.RetrieveAPIView):
    queryset = TeacherTechnology.objects.all()
    serializer_class = TeacherTechnologySerializer

    @extend_schema(
        summary="Детальная информация Технологии Проподователя",
        description="Детальная информация Технологии Проподователя",
        responses={200: TeacherTechnologySerializer()},
        operation_id="detail_teacher_technology_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#=================================================================
class ClassesGoingListView(generics.ListAPIView):
    queryset = ClassesGoing.objects.all()
    serializer_class = ClassGoingSerializer
    
class ClassesGoingDetailView(generics.RetrieveAPIView):
    queryset = ClassesGoing.objects.all()
    serializer_class = ClassGoingSerializer


#=================================================================

class ClassGoingListTopik(generics.ListAPIView):
    queryset = ClassGoingTopik.objects.all()
    serializer_class = ClassGoingTopikSerializer

class ClassGoingDetailTopik(generics.RetrieveAPIView):
    queryset = ClassGoingTopik.objects.all()
    serializer_class = ClassGoingTopikSerializer