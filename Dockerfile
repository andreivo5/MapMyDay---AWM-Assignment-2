FROM continuumio/miniconda3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

COPY ENV.yml .
RUN conda env create -f ENV.yml && conda clean -afy

SHELL ["conda", "run", "-n", "awm_env", "/bin/bash", "-c"]

EXPOSE 8000

CMD ["conda", "run", "-n", "awm_env", "python", "mapmyday/manage.py", "runserver", "0.0.0.0:8000"]
