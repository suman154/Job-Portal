import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job, Company, Application

class CompanyType(DjangoObjectType):
    class Meta:
        model = Company

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application

class Query(graphene.ObjectType):
    all_jobs = graphene.List(JobType)
    job = graphene.Field(JobType, id=graphene.Int())
    all_companies = graphene.List(CompanyType)

    def resolve_all_jobs(self, info):
        return Job.objects.all()

    def resolve_job(self, info, id):
        return Job.objects.get(pk=id)

    def resolve_all_companies(self, info):
        return Company.objects.all()

class CreateApplication(graphene.Mutation):
    application = graphene.Field(ApplicationType)

    class Arguments:
        job_id = graphene.Int()
        applicant_name = graphene.String()
        cover_letter = graphene.String()

    def mutate(self, info, job_id, applicant_name, cover_letter):
        job = Job.objects.get(pk=job_id)
        application = Application(job=job, applicant_name=applicant_name, cover_letter=cover_letter)
        application.save()
        return CreateApplication(application=application)

class Mutation(graphene.ObjectType):
    create_application = CreateApplication.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
