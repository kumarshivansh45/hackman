from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models,auth
from database import engine
from routers import captchas,tfa,user
# , auth, vote,post
# from routers import user, language, message, articles, data_conf, surveys, ads, fxn_config, forensics, system_conf, universal_app_data, buses, stoppages, trip_routes, journey, tracking
from config import Settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(captchas.router)
app.include_router(tfa.router)
app.include_router(user.router)
app.include_router(auth.router)

# app.include_router(post.router)
# app.include_router(user.router)
# app.include_router(language.router)
# app.include_router(message.router)
# app.include_router(data_conf.router)
# app.include_router(articles.router)
# app.include_router(surveys.router)
# app.include_router(ads.router)
# app.include_router(fxn_config.router)
# app.include_router(forensics.router)
# app.include_router(system_conf.router)
# app.include_router(universal_app_data.router)
# app.include_router(buses.router)
# app.include_router(stoppages.router)
# app.include_router(trip_routes.router)
# app.include_router(journey.router)
# app.include_router(tracking.router)


# app.include_router(vote.router)
