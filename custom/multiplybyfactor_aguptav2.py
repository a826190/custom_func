import logging

from iotfunctions import ui
from iotfunctions.base import BaseTransformer
import pandas as pd

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'git+https://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@github.com/a826190/custom_func.git@starter_package'


class MultiplyByFactor_aguptav2(BaseTransformer):

    def __init__(self, input_items, factor, output_items):

        self.input_items = input_items
        self.output_items = output_items
        self.factor = float(factor)
        super().__init__()
    def execute(self, df):
        df = df.copy()
        #df_temp=pd.DataFrame()
        df['distance']=df['speed']*df['travel_time']


        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
                name = 'input_items',
                datatype=float,
                description = "Data items adjust",

                )
                      )

        outputs = [
            ui.UIFunctionOutSingle(name='distance_ot', datatype=float, description='Output distance')]
        return (inputs,outputs)