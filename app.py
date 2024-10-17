
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

from Bank_Marketing.constants import APP_HOST, APP_PORT
from Bank_Marketing.pipline.prediction_pipeline import BankmarketingData, BankClassifier
from Bank_Marketing.pipline.training_pipeline import TrainPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.job: Optional[str] = None
        self.education: Optional[str] = None
        self.marital: Optional[str] = None
        self.default: Optional[str] = None
        self.housing: Optional[str] = None
        self.loan: Optional[str] = None
        self.month: Optional[str] = None
        self.day_of_week: Optional[str] = None
        self.poutcome: Optional[str] = None
        self.age: Optional[str] = None
        self.duration: Optional[str] = None
        self.campaign: Optional[str] = None
        self.pdays: Optional[str] = None
        self.previous: Optional[str] = None
        self.emp_var_rate: Optional[str] = None  
        self.cons_price_idx: Optional[str] = None  
        self.cons_conf_idx: Optional[str] = None  
        self.euribor3m: Optional[str] = None
        self.nr_employed: Optional[str] = None
        self.contact: Optional[str] = None

        

    async def get_bank_data(self):
        form = await self.request.form()
        self.job = form.get("job")
        self.education = form.get("education")
        self.marital = form.get("marital")
        self.default = form.get("default")
        self.housing = form.get("housing")
        self.loan = form.get("loan")
        self.month = form.get("month")
        self.day_of_week = form.get("day_of_week")
        self.poutcome = form.get("poutcome")
        self.age = form.get("age")
        self.duration = form.get("duration")
        self.campaign = form.get("campaign")
        self.pdays = form.get("pdays")
        self.previous = form.get("previous")
        self.emp_var_rate = form.get("emp_var_rate")  # Adjusted for mapping
        self.cons_price_idx = form.get("cons_price_idx")  # Adjusted for mapping
        self.cons_conf_idx = form.get("cons_conf_idx")  # Adjusted for mapping
        self.euribor3m = form.get("euribor3m")
        self.nr_employed = form.get("nr_employed")  # Adjusted for mapping
        self.contact = form.get("contact")

@app.get("/", tags=["authentication"])
async def index(request: Request):

    return templates.TemplateResponse(
            "bank.html",{"request": request, "context": "Rendering"})


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/")
async def predictRouteClient(request: Request):
    try:
        form = DataForm(request)
        await form.get_bank_data()
        # Debugging outputs
        print(f"Retrieved form data: {form.__dict__}")
        bank_data = BankmarketingData(
                                job=form.job,
                                education=form.education,
                                marital=form.marital,
                                default=form.default,
                                housing=form.housing,
                                loan=form.loan,
                                month=form.month,
                                day_of_week=form.day_of_week,
                                poutcome=form.poutcome,
                                age=form.age,
                                duration=form.duration,
                                campaign=form.campaign,
                                pdays=form.pdays,
                                previous=form.previous,
                                emp_var_rate=form.emp_var_rate,  # Using underscore
                                cons_price_idx=form.cons_price_idx,  # Using underscore
                                cons_conf_idx=form.cons_conf_idx,  # Using underscore
                                euribor3m=form.euribor3m,
                                nr_employed=form.nr_employed,  # Using underscore
                                contact=form.contact

                                )
        
        bank_df = bank_data.get_bank_input_data_frame()

        model_predictor = BankClassifier()

        value = model_predictor.predict(dataframe=bank_df)[0]

        print(f"Prediction Value: {value}")

        status = None
        if value == 1:
            status = "Term Deposit Subscribed:"
        else:
            status = "Term Deposit Not Subscribed:"

        return templates.TemplateResponse(
            "bank.html",
            {"request": request, "context": status},
        )
        
    except Exception as e:
        return templates.TemplateResponse(
            "bank.html",
            {"request": request, "context": f"Error: {str(e)}"},
        )
        #return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)